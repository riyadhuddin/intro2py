import molmass

def calculate_atomic_mass(molecule: str) -> float:
    """Calculates the atomic mass of a molecule.

    Args:
        molecule: A string representing the molecular formula of the molecule.

    Returns:
        The atomic mass of the molecule.
    """
    # Parse the molecular formula
    formula = molmass.Formula(molecule)

    # Calculate the atomic mass
    atomic_mass = formula.isotope.mass

    return atomic_mass

print(calculate_atomic_mass("O"))  # Outputs: 18.010565
print(calculate_atomic_mass("C2"))  # Outputs: 44.0095
print(calculate_atomic_mass("C6H12O6"))  # Outputs: 180.156
