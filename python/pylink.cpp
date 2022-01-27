#define PY_SSIZE_T_CLEAN
#pragma once
#include <Python.h>


// Exported methods are collected in a table
static struct PyMethodDef method_table[] = {
    {NULL,
     NULL,
     0,
     NULL} // Sentinel value ending the table
};

// A struct contains the definition of a module
static PyModuleDef bimgPy_module = {
    PyModuleDef_HEAD_INIT,
    "bimgPy", // Module name
    "bimgPy",
    -1, // Optional size of the module state memory
    method_table,
    NULL, // Optional slot definitions
    NULL, // Optional traversal function
    NULL, // Optional clear function
    NULL  // Optional module deallocation function
};

// The module init function
PyMODINIT_FUNC PyInit_bimgPy(void)
{
    return PyModule_Create(&bimgPy_module);
}