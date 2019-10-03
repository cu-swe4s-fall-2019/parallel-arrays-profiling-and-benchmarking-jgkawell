import unittest
import data_viz
import random
import os


class TestMathLib(unittest.TestCase):

    """ BOXPLOT TESTS """

    def test_boxplot_file_already_exists(self):
        file_name = "test.png"
        f = open(file_name, "w+")
        f.close()

        with self.assertRaises(FileExistsError) as ex:
            data_viz.boxplot([], file_name)

        self.assertEqual(str(ex.exception), "That file name already exists.")

        os.remove(file_name)

    def test_boxplot_random_int_array(self):
        file_name = "test.png"
        rand_int_list = [random.randrange(-1000, 1000) for i in range(1000)]
        data_viz.boxplot(rand_int_list, file_name)

        self.assertEqual(os.path.exists(file_name), True)

        os.remove(file_name)

    def test_boxplot_random_double_array(self):
        file_name = "test.png"
        rand_double_list = [random.random() for i in range(1000)]
        data_viz.boxplot(rand_double_list, file_name)

        self.assertEqual(os.path.exists(file_name), True)

        os.remove(file_name)

    """ HISTOGRAM TESTS """

    def test_histogram_file_already_exists(self):
        file_name = "test.png"
        f = open(file_name, "w+")
        f.close()

        with self.assertRaises(FileExistsError) as ex:
            data_viz.histogram([], file_name)

        self.assertEqual(str(ex.exception), "That file name already exists.")

        os.remove(file_name)

    def test_histogram_random_int_array(self):
        file_name = "test.png"
        rand_int_list = [random.randrange(-1000, 1000) for i in range(1000)]
        data_viz.histogram(rand_int_list, file_name)

        self.assertEqual(os.path.exists(file_name), True)

        os.remove(file_name)

    def test_histogram_random_double_array(self):
        file_name = "test.png"
        rand_double_list = [random.random() for i in range(1000)]
        data_viz.histogram(rand_double_list, file_name)

        self.assertEqual(os.path.exists(file_name), True)

        os.remove(file_name)

    """ COMBO TESTS """

    def test_combo_file_already_exists(self):
        file_name = "test.png"
        f = open(file_name, "w+")
        f.close()

        with self.assertRaises(FileExistsError) as ex:
            data_viz.combo([], file_name)

        self.assertEqual(str(ex.exception), "That file name already exists.")

        os.remove(file_name)

    def test_combo_random_int_array(self):
        file_name = "test.png"
        rand_int_list = [random.randrange(-1000, 1000) for i in range(1000)]
        data_viz.combo(rand_int_list, file_name)

        self.assertEqual(os.path.exists(file_name), True)

        os.remove(file_name)

    def test_combo_random_double_array(self):
        file_name = "test.png"
        rand_double_list = [random.random() for i in range(1000)]
        data_viz.combo(rand_double_list, file_name)

        self.assertEqual(os.path.exists(file_name), True)

        os.remove(file_name)


if __name__ == '__main__':
    unittest.main()
