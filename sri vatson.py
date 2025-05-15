import random
import time
import matplotlib.pyplot as plt

MAX_TEMPERATURE = 75.0
MAX_WEIGHT = 10.0

class Product:
    def __init__(self, id):
        self.id = id
        self.temperature = round(random.uniform(65.0, 85.0), 2)
        self.weight = round(random.uniform(8.0, 12.0), 2)
        self.passed = None

    def perform_quality_check(self):
        if self.temperature <= MAX_TEMPERATURE and self.weight <= MAX_WEIGHT:
            self.passed = True
        else:
            self.passed = False

    def __str__(self):
        status = "PASS" if self.passed else "FAIL"
        return (f"Product {self.id}: Temp={self.temperature}°C, "
                f"Weight={self.weight}kg -> {status}")

def run_quality_control(batch_size=10):
    print("Starting Quality Control Simulation...\n")
    pass_count = 0
    fail_count = 0

    for i in range(1, batch_size + 1):
        product = Product(id=i)
        product.perform_quality_check()
        print(product)

        if product.passed:
            pass_count += 1
        else:
            fail_count += 1

        time.sleep(0.5)

    print(f"\nSummary: {pass_count} Passed, {fail_count} Failed.")
    plot_results(pass_count, fail_count)

def plot_results(pass_count, fail_count):
    labels = ['Passed', 'Failed']
    counts = [pass_count, fail_count]
    colors = ['green', 'red']

    plt.figure(figsize=(6, 4))
    plt.bar(labels, counts, color=colors)
    plt.title('Quality Control Results')
    plt.xlabel('Result')
    plt.ylabel('Number of Products')
    plt.ylim(0, max(counts) + 2)

    # Annotate bars with values
    for i, v in enumerate(counts):
        plt.text(i, v + 0.1, str(v), ha='center', fontweight='bold')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_quality_control()
