"""
Program: InvestmentGUI.py
Author:  Jordyn  7/14/2023

GUI-based version of the investment calculator app from Chapter 3. Also illustarates the use of the text Area component.

NOTE: The file breezypythongui.py MUST be in the same directory as this file for the app to run correctly
"""

from breezypythongui import EasyFrame
# Other imports go here

# Class header (application name will change project to project)
class TextAreaDemo(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		# Call to the Easy Frame constrctor method
		EasyFrame.__init__(self, title = "Investment Calculator")
		# Create and add the components to the window
		self.addLabel(text = "Initial Amount", row= 0, column = 0)
		self.addLabel(text = "Number of Years", row = 1, column = 0)
		self.addLabel(text = "Interest Rate in %", row = 2, column = 0)

		self.amount = self.addFloatField(value = 0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1, width = 20)
		self.rate = self.addFloatField(value = 0.0, row = 2, column = 1)

		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		self.compute["background"] = "yellow"
		self.compute["foreground"] = "red"
		self.compute["width"] = 21

	# Definition of the compute() funtion
	def compute(self):
		# Obtain and validate the inputs
		startBalance = self.amount.getNumber()
		years = self.period.getNumber()
		rate = self.rate.getNumber() / 100 

		if startBalance == 0 or years == 0 or rate == 0: 
			return

		# Initialize the accumlator variable for the interest over time
		totalInterest = 0.0

		# Display the header in tabular format for the output
		result = "%4s%18s%10s%16s" % ("Year", "Starting Balance", "Interest", "Ending Balance")

		# Compute and append the results for each year
		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest

		# Append the totals for the entire investment period
		result += "Ending balance: $%0.2f\n" % endBalance
		result += "Total interest earned: $%0.2f\n" % totalInterest

		# Output the final result
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"

# Global definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
	TextAreaDemo().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()