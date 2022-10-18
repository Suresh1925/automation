# When a Python script encounters a situation that it cannot cope with, it raises an exception. 
# An exception is a Python object that represents an error.


# at first cart will be zero
ItemsInCart = 0
# 2 items will be added to cart
# after adding if cart is zero,
if ItemsInCart != 2:
    pass
    # raise Exception("Products cart count not matching")


#If the expression is false, Python raises an AssertionError exception.
assert(ItemsInCart == 2)

