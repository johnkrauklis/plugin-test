# Architecture

## Overview

A single-file cart calculator. No classes, no discount abstraction — pricing
logic lives directly in two functions.

## Components

**calculate_total()** — the only place discount and tax math happens for a
general cart. Takes an optional flat discount percentage.

**apply_member_discount()** — a separate, hardcoded 10% discount path for
members. Duplicates the tax/discount arithmetic from calculate_total() rather
than calling it.

## Boundaries

There is no shared discount logic. Any change to how tax or discounts are
calculated has to be made in both functions by hand.
