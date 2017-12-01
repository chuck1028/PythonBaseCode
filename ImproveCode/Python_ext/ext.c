#include "Python.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//纯C扩展代码
//创建应用代码
int fac(int n){
    if (n < 2){
        return 1;
    }
    else{
        return fac(n - 1) + fac(n - 2);
    }
}

char * reverse(char *s){
    char t;
    char *p = s;
    char *q = (s + (strlen(s) - 1));

   while (p < q){
       t = *p;
       *p++ = *q;
       *q-- = t;
   }

    return s;
}

int test(void){
    char s[64] = {};

    printf("4! = %d\n", fac(4));
    printf("8! = %d\n", fac(8));
    printf("12! = %d\n", fac(12));

    strcpy(s, "abcdef");
    printf("reverse1 = %s\n", reverse(s));

    strcpy(s, "123456");
    printf("reverse2 = %s\n", reverse(s));

    return 0;
}

//根据样板代码编写封装代码
//1. 包含Python.h头文件
//2. 为函数编写形如 P月Object *Module_func()的封装函数
static PyObject * ext_fac(PyObject *self, PyObject *args){
    int res =0;
    int num =0;
    PyObject *retval = NULL;

    res = PyArg_ParseTuple(args, "i", &num);
    if (!res){
        return NULL;
    }

    res = fac(num);
    retval = (PyObject *)Py_BuildValue("i", res);

    return retval;
}

static PyObject * ext_doppel(PyObject *self, PyObject *args){
    char *orig_str = NULL;

    if (!PyArg_ParseTuple(args, "s", &orig_str)){
         return NULL;
    }
    
    return (PyObject *)Py_BuildValue("ss", orig_str, reverse(strdup(orig_str)));
}

//3. 为模块编写 PyMethodDef ModuleMethods[] 数组
static PyMethodDef extMethods[] = {
    {"fac", ext_fac, METH_VARARGS},    //METH_VARARGS 表示参数以元组形式给定
    {"doppel", ext_doppel, METH_VARARGS},
    {NULL, NULL},
};

//4. 添加模块初始化函数 void initModule()
void initext(void){
    Py_InitModule("ext", extMethods);
}

