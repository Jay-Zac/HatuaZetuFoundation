import paypalrestsdk
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DonationForm
from .models import Donation


def create_payment(request):
    # Handle POST request to create a PayPal payment
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            try:
                donation = form.save(commit=False)  # Prepare donation data without saving
                payment = paypalrestsdk.Payment({
                    "intent": "sale",  # Payment intent (sale indicates an immediate payment)
                    "payer": {"payment_method": "paypal"},
                    "redirect_urls": {
                        # URL to redirect on success
                        "return_url": request.build_absolute_uri('/donations/payment-executed/'),
                        # URL to redirect on cancel
                        "cancel_url": request.build_absolute_uri('/donations/payment-cancelled/')
                    },
                    "transactions": [{
                        "item_list": {
                            "items": [{
                                "name": "Donation to Hatua Zetu Foundation",  # Name of the donation item
                                "sku": "donation",  # Stock keeping unit identifier
                                "price": str(donation.amount),  # Convert donation amount to string for PayPal
                                "currency": "USD",  # Currency in which the donation is made
                                "quantity": 1  # Quantity of items (always 1 for donations)
                            }]
                        },
                        "amount": {
                            "total": str(donation.amount),  # Total amount for the transaction
                            "currency": "USD"  # Currency for the total amount
                        },
                        "description": f"Donation by {donation.name}"  # Description of the transaction
                    }]
                })

                if payment.create():  # Attempt to create the payment on PayPal
                    request.session['payment_id'] = payment.id  # Save payment ID for later use
                    for link in payment.links:
                        if link.rel == "approval_url":
                            return redirect(link.href)  # Redirect to PayPal for approval
                else:
                    # Notify of failure
                    messages.error(request, "Payment processing failed. Try again.")
                    # Render error page
                    return render(request, 'donations_html/error.html', {'error': payment.error})

            except Exception as e:
                # Notify of unexpected errors
                messages.error(request, "Unexpected error occurred. Try again later.")
                # Render error page
                return render(request, 'donations_html/error.html', {'error': str(e)})
        else:
            messages.error(request, "Please correct the errors below.")  # Notify of form validation errors
    else:
        form = DonationForm()  # Create an empty form for GET requests
    # Render donation page with form
    return render(request, 'donations_html/donate.html', {'form': form})


def execute_payment(request):
    # Handle the execution of a PayPal payment after user approval
    payment_id = request.session.get('payment_id')
    payer_id = request.GET.get('PayerID')

    if not payment_id or not payer_id:
        messages.error(request, "Incomplete payment information. Try again.")  # Notify of missing info
        return redirect('donations:donate')  # Redirect to donation page

    try:
        payment = paypalrestsdk.Payment.find(payment_id)  # Find the payment using PayPal SDK
        if payment.execute({"payer_id": payer_id}):  # Execute the payment
            # Create a donation record in the database
            donation = Donation.objects.create(
                name=payment.payer.payer_info.first_name,
                email=payment.payer.payer_info.email,
                amount=payment.transactions[0].amount.total,
                message="Donation via PayPal"
            )
            donation.save()  # Save the donation record to the database
            messages.success(request, "Thank you for your donation!")  # Notify of successful donation
            return redirect('donations:thank_you')  # Redirect to thank-you page
        else:
            # Notify of failure
            messages.error(request, "Payment execution failed. Try again.")
            # Render error page
            return render(request, 'donations_html/error.html', {'error': payment.error})

    except paypalrestsdk.ResourceNotFound:
        messages.error(request, "Payment not found. Try again.")  # Notify if payment is not found
        return redirect('donations:donate')  # Redirect to donation page

    except Exception as e:
        # Notify of unexpected errors
        messages.error(request, "Unexpected error occurred. Try again later.")
        # Render error page
        return render(request, 'donations_html/error.html', {'error': str(e)})


def payment_executed(request):
    # Render the thank-you page after a successful payment
    return render(request, 'donations_html/thank_you.html')  # Render thank-you template


def payment_cancelled(request):
    # Render the cancellation page if the payment is cancelled
    return render(request, 'donations_html/cancelled.html')  # Render cancellation template
