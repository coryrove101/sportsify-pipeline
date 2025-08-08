import unittest
from src.model.neural_network import NeuralNetwork

class TestNeuralNetwork(unittest.TestCase):

    def setUp(self):
        self.model = NeuralNetwork(input_size=10, hidden_size=5, output_size=1)

    def test_initialization(self):
        self.assertIsNotNone(self.model.weights_input_hidden)
        self.assertIsNotNone(self.model.weights_hidden_output)

    def test_forward_pass(self):
        input_data = [0.5] * 10
        output = self.model.forward_pass(input_data)
        self.assertEqual(len(output), 1)

    def test_training(self):
        training_data = [[0.5] * 10, [0.2] * 10]
        target_data = [[1], [0]]
        self.model.train(training_data, target_data, epochs=10)
        self.assertTrue(self.model.loss < 0.1)

if __name__ == '__main__':
    unittest.main()