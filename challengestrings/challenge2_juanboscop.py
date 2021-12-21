#temperature coverter app
print("\nWelcome to bosco's temperature converter program\n")

temperature = float(input("Enter the temperature in Farenheit: "))

celsius = round((temperature - 32)* 5/9,4)
kelvin = round((temperature - 32)* 5/9 + 273.15,4)
print(f"""
      \n this is {temperature} Farenheit
      \n this is {celsius} celsius
      \n this is {kelvin} kelvin
                                        """)
      
