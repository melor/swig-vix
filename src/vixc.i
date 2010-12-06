%module vixc
%include cpointer.i
%{
/* Includes the header in the wrapper code */
#define SWIG_FILE_WITH_INIT 1
#include "vmware-vix/vix.h"
%}

/* Parse the header file to generate wrappers */
%include "vmware-vix/vix.h"
%pointer_functions(VixPropertyID, VixPropertyIDp);


