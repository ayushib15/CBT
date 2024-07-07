from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_receipt(customer_name, amount_paid, payment_method, receipt_number, filename):
    # Create canvas
    c = canvas.Canvas(filename, pagesize=letter)

    # Set font
    c.setFont("Helvetica", 12)

    # Write receipt details
    c.drawString(100, 750, "Receipt Number: " + receipt_number)
    c.drawString(100, 730, "Customer Name: " + customer_name)
    c.drawString(100, 710, "Amount Paid: $" + str(amount_paid))
    c.drawString(100, 690, "Payment Method: " + payment_method)

    # Draw line
    c.line(50, 680, 550, 680)

    # Thank you message
    c.drawString(100, 660, "Thank you for your payment!")

    # Save PDF
    c.save()

    print("Receipt generated successfully.")

if __name__ == "__main__":
    customer_name = input("Enter customer name: ")
    amount_paid = float(input("Enter amount paid: "))
    payment_method = input("Enter payment method: ")
    receipt_number = input("Enter receipt number: ")
    filename = input("Enter filename to save receipt (without extension): ") + ".pdf"

    generate_receipt(customer_name, amount_paid, payment_method, receipt_number, filename)

