#!/usr/bin/python3
from numpy import matmul
"""Lazy matrix multiplication using numpy library"""

def lazy_matrix_mul(m_a, m_b):
    """lazy multiplication
    Arguments:
        m_a ([[]]): first matrix
        m_b ([[]]): second matrix
    """
    return(matmul(m_a, m_b))
