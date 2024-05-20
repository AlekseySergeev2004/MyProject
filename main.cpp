// main.cpp

/**
 * \file main.cpp
 * \brief A simple example of documented code.
 *
 * This is a simple example of how to document C++ code using Doxygen.
 */

/**
 * \brief Adds two integers.
 * \param a The first integer.
 * \param b The second integer.
 * \return The sum of a and b.
 */
int add(int a, int b) {
    return a + b;
}

/**
 * \brief The main function.
 * \return Exit status.
 */
int main() {
    int result = add(2, 3);
    return 0;
}
