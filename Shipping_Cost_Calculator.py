# Shipping Cost Calculator can you read this? probalby not this is jyst a comment for developers
## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: ")) #crazy how you don't have to pre specify what type of data weight is
rate = float(input("Enter the shipping rate per kilogram: "))
## Calculate shipping cost
shipping_cost = weight * rate
## Display the result
print(f"Shipping Cost: {shipping_cost} USD")   #frieren take notes: in phython to add a variable in print u use the {} and most likely you have to have the text preceded by f (to underline how it it formatted text? 
#and therefore {} should not be read literally? Maybe
