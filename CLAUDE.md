# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a collection of Jupyter Notebooks for an **introductory Python programming course** ("Introdução à Programação com Python") taught as part of the Stellantis Residency program at CIn-UFPE. All content is in **Brazilian Portuguese**.

The notebooks are designed to be used with **Google Colab** (linked from README.md with Colab badges).

## Repository Structure

Notebooks are organized in numbered topic directories, following the course progression:

- `01_Desafios/` – Initial challenges (images only, no notebooks)
- `02_Intro_Programacao/` – Intro to programming concepts (README only)
- `03_Intro_Python/` – Python introduction
- `04_Variaveis_Expressoes_Declaracoes/` – Variables, expressions, statements
- `05_Comandos_Condicionais/` – Conditionals (if/else), includes a Nuclear Reactor exercise
- `06_Laços/` – Loops (for, while)
- `07_Listas/` – Lists
- `08_Tuplas_Dicionarios/` – Tuples and dictionaries
- `09_Funcoes/` – Functions
- `10_Regex/` – Regular expressions
- `11_Dados_Visualizacao/` – Data handling (Pandas, NumPy, JSON) with CSV datasets
- `imagens/` – Legacy shared images directory

## Notebook Naming Convention

Each topic directory typically contains up to three notebook variants:
- **`Topic.ipynb`** – Complete version with all content and solutions (instructor reference)
- **`Topic_para_preencher.ipynb`** – "Fill-in" version with blanks for students to complete during class
- **`Topic_preenchido_24_2.ipynb`** – Filled-in version from the 2024.2 semester

When creating or editing notebooks, maintain this three-variant pattern.

## Working with Notebooks

- Notebooks use standard Python 3 and common libraries (pandas, numpy, matplotlib)
- The `11_Dados_Visualizacao/` directory contains CSV data files used by the Pandas notebooks
- The `ColabTurtlePlus_Primeiros_Passos.ipynb` at the root uses the `ColabTurtlePlus` library for the initial challenge
- Each topic directory has an `imgs/` subfolder for topic-specific images referenced in notebooks

## Key Conventions

- All instructional text, markdown cells, and comments are written in **Brazilian Portuguese**
- Image references in notebooks use relative paths to the local `imgs/` subfolder within each topic directory
- The GitHub repo is `filipecalegario/intro-programacao-python` on the `main` branch
- Colab links follow the pattern: `https://colab.research.google.com/github/filipecalegario/intro-programacao-python/blob/main/<path>`
