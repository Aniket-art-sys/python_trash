coeff = [int(input(f"enter {i}: ")) for i in ["a", "b", "c"]]
root1 = (-coeff[1] + ((coeff[1]**2) - (4 * coeff[0] * coeff[2]))**0.5) / (2 * coeff[0])
root2 = (-coeff[1] - ((coeff[1]**2) - (4 * coeff[0] * coeff[2]))**0.5) / (2 * coeff[0])

print("The roots are:", root1, root2)
