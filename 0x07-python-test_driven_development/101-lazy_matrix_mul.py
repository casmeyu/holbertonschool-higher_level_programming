#!/usr/bin/python3
"""Lazy matrix multiplication using numpy library"""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """lazy multiplication
    Arguments:
        m_a ([[]]): first matrix
        m_b ([[]]): second matrix
    """
    return(matmul(m_a, m_b))
