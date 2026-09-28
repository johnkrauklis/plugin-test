# Architecture

## Overview

A single-file cart calculator. No classes, no discount abstraction — pricing
logic lives directly in two functions.

## Components

**calculate_total()** — the only place discount and tax math happens for a
general cart. Takes an optional flat discount percentage.

**apply_member_discount()** — calls calculate_total() with a hardcoded 10%
discount for members.

## Boundaries

All discount and tax math is centralized in calculate_total(). Both call
sites share the same logic, so a fix in one place applies everywhere.
