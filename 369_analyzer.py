class TeslaAnalyzer:
    def __init__(self):
        self.core_numbers = [3, 6, 9]
        self.properties = {
            3: {'role': 'generator', 'phase': 'start', 'polarity': 'yang'},
            6: {'role': 'transformer', 'phase': 'middle', 'polarity': 'yin'},
            9: {'role': 'completion', 'phase': 'end', 'polarity': 'yang'}
        }

    def digital_root(self, n):
        """Calculate digital root using modulo method"""
        return n if n < 10 else n % 9 or 9

    def analyze(self, number, depth=9):
        """Generate comprehensive pattern analysis"""
        return {
            'base': {
                'number': number,
                'properties': self.properties.get(number, {}),
                'digital_root': self.digital_root(number)
            },
            'sequences': {
                'multiplication': self._get_multiplication_sequence(number, depth),
                'vortex': self._get_vortex_sequence(number, depth),
                'doubling': self._get_doubling_sequence(number, depth)
            }
        }

    def _get_multiplication_sequence(self, n, depth):
        """Generate multiplication pattern"""
        return [self.digital_root(n * i) for i in range(1, depth + 1)]

    def _get_vortex_sequence(self, n, depth):
        """Generate vortex pattern (adding the number to itself)"""
        sequence = []
        current = n
        for _ in range(depth):
            sequence.append(current)
            current = self.digital_root(current + n)
        return sequence

    def _get_doubling_sequence(self, n, depth):
        """Generate doubling pattern"""
        sequence = []
        current = n
        for _ in range(depth):
            sequence.append(current)
            current = self.digital_root(current * 2)
        return sequence


# Example usage
if __name__ == "__main__":
    analyzer = TeslaAnalyzer()

    # Analyze each core number
    for number in [3, 6, 9]:
        result = analyzer.analyze(number)
        print(f"\nAnalysis for number {number}:")
        print(f"Role: {result['base']['properties']['role']}")
        print(f"Phase: {result['base']['properties']['phase']}")
        print(f"Polarity: {result['base']['properties']['polarity']}")
        print(f"Digital Root: {result['base']['digital_root']}")
        print(f"Multiplication Sequence: {result['sequences']['multiplication'][:6]}")
        print(f"Vortex Sequence: {result['sequences']['vortex'][:6]}")
        print(f"Doubling Sequence: {result['sequences']['doubling'][:6]}")
