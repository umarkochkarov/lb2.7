#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"a", "b", "f", "g", "i"}
    b = {"c", "f", "g", "i", "s", "u"}
    c = {"a", "g", "h", "i"}
    d = {"f", "w", "x"}
    x = (a.intersection(b)).union(c)
    print(f"x = {x}")
    # Найдем дополнения множеств
    bn = u.difference(b)
    y = (a.intersection(bn)).union(c.difference(b))
    print(f"y = {y}")