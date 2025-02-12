# NumPy Fundamentals and Array Operations
## PLUS W - IT Training
*Date: February 13, 2025*

---

## 1. Class Code Overview
The class code demonstrates NumPy fundamentals and array operations, providing essential concepts for scientific computing and data analysis.

### Core Concepts Covered

1. **NumPy Basics**
   - Python lists vs NumPy arrays
   - Array creation methods
   - Data types and structures
   - Array dimensions

2. **Array Creation**
   - Basic array initialization
   - Arrays with zeros and ones
   - Arrays with specific values
   - Random array generation
   - Evenly spaced arrays

3. **Array Properties**
   - Shape and size
   - Dimensions
   - Data types
   - Array transformation
   - Reshaping operations

4. **Array Operations**
   - Basic arithmetic
   - Array mathematics
   - Broadcasting
   - Statistical operations
   - Conditional operations

5. **Array Indexing**
   - Basic indexing
   - Slicing operations
   - Advanced indexing
   - Boolean indexing
   - Fancy indexing

---

## 2. Code Examples

### Basic Array Operations
```python
# Creating arrays
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Special arrays
zeros_array = np.zeros((2, 3))
ones_array = np.ones((2, 3))
full_array = np.full((2, 3), 8)

# Random arrays
random_array = np.random.rand(3, 3)
random_int_array = np.random.randint(1, 100, (3, 3))
```

### Array Manipulation
```python
# Shape and size
print(arr.shape)  # Array dimensions
print(arr.size)   # Total elements

# Reshaping
arr_reshaped = arr.reshape((2, 3))

# Slicing
arr[:, 1:3]  # All rows, columns 1 to 2

# Conditional operations
result = np.where(arr1 > 10)
```

---

## 3. Functions as First-Class Objects

### Key Concepts
1. **Function Assignment**
   - Assigning functions to variables
   - Function references

2. **Function Arguments**
   - Passing functions as parameters
   - Returning functions
   - Function composition

3. **Scoping**
   - Local variables
   - Global variables
   - Nonlocal variables

4. **Documentation**
   - Docstrings
   - Function documentation
   - Help system usage

---

## 4. Best Practices
1. Use appropriate array creation methods
2. Understand broadcasting rules
3. Optimize array operations
4. Handle memory efficiently
5. Use vectorized operations
6. Implement proper error handling
7. Document array shapes and types

---

## 5. Learning Objectives
By the end of this class, students should be able to:
- Create and manipulate NumPy arrays
- Perform array operations efficiently
- Understand array indexing and slicing
- Implement basic data analysis
- Use NumPy's mathematical functions
- Apply array transformations
- Handle multi-dimensional arrays

---

## 6. Resources
1. **Documentation**
   - NumPy Official Documentation
   - Array Operations Guide
   - Broadcasting Rules

2. **Tools**
   - Python development environment
   - Jupyter Notebooks
   - NumPy library

3. **Additional Reading**
   - Scientific Computing with Python
   - Array Programming Concepts
   - Performance Optimization

---

## Common Operations Reference

### Array Creation
```python
np.array([1, 2, 3])           # From list
np.zeros((3, 3))              # Zero array
np.ones((3, 3))               # Ones array
np.random.rand(3, 3)          # Random array
np.linspace(1, 10, 5)         # Evenly spaced
```

### Array Operations
```python
arr.sum()                     # Sum of elements
arr.mean()                    # Mean of elements
arr.max()                     # Maximum value
arr.min()                     # Minimum value
arr.reshape((2, 3))          # Reshape array
```

---

*Note: This documentation provides an overview of NumPy fundamentals and array operations. For detailed implementation examples, refer to the class code and exercises.*