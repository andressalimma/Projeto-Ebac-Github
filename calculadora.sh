#!/bin/bash

read -p "Digite o primeiro número: " num1
read -p "Digite o operador (+, -, *, /): " operador
read -p "Digite o segundo número: " num2
resultado=$(echo "$num1 $operador $num2" | bc)
echo "Resultado: $resultado"

