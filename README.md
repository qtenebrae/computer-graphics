# Oval

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Github CI](https://github.com/qtenebrae/computer-graphics/actions/workflows/python-app.yml/badge.svg)](https://github.com/qtenebrae/computer-graphics/actions/workflows/python-app.yml)

Oval is an application designed to draw an ellipse with the possibility of moving it on the canvas. It is also possible
to fill the ellipse with different colours.

## Content

- [Intro](#intro)
- [Getting started](#getting-started)
    - [Installation](#installation)
- [Running the app](#running-the-app)
- [Project usage](#project-usage)

## Intro

The project was written as part of the Computer Graphics laboratory work.

You can see the app in action in the gif below.

<p align="center">
  <img src="https://github.com/qtenebrae/computer-graphics/blob/main/img/presentation.gif" width="600" height="500">
</p>

## Getting started

### Installation

Clone the repository

    git clone https://github.com/qtenebrae/computer-graphics.git

Switch to the repo folder

    cd computer-graphics

Installing dependencies

    pip install pytest

## Running the app

To run the application, you need to write a script:

    python .\src\__init__.py

To run the tests, it is sufficient to write the following:

    pytest

## Project usage

When the application is started for the semi-major axes A and B, the coordinates of the centre are set to default
values.

These values can be changed by the user.

The ellipse is drawn by pressing either the `Рисовать` button or the `Enter` key.

Pressing the `Up`, `Down`, `Left`, `Right` keys moves the ellipse by the specified step in the corresponding direction.

The ellipse fill colour can be changed to next / previous by pressing the `bracketleft` / `bracketleft` keys
respectively.
