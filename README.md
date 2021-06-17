# arc_solver

A class for solving circular geometry where radius and the length of arc is known.

## What can it do?

Provide information on the following -

* Sagitta
* Chord length
* Apothem of the arc
* And more.

## Graphing

The class provides graphing functionality for calculating the coordinates for representing the circular arc on a graph.

It is designed so that the beginning and the end of the arc will be graphed resting on the x axis. This allows the rise
and fall of the arc to be used for representing things such as the curvature of the earth etc.

See https://github.com/MHenderson1988/line-of-sight-analysis as an example of how this can be used.

## Quick start

ArcSolver(radius, arc_length, samples=)

samples will default to 150 if no input is given. It defines how many coordinate points will be generated for later use.

```bazaar
from arc_solver import ArcSolver

# Example of creating a circle of radius 1, with an arc_length of 1

arc = ArcSolver(1,1, samples=100)
```

## Attributes

The ArcSolver class has the following attributes which can be accessed after being instantiated.

* .radians
* .chord_length
* .degrees
* .sagitta
* .arc_apothem
* .circular_centre_x
* .circular_centre_y
* .diameter
* .start_angle
* .end_angle
* .angles_list
* .x_coordinates
* .y_coordinates