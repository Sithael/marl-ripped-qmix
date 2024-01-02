# MARLware: Modular Multi-Agent Reinforcement Learning

Welcome to Marl-Engineering, a repository dedicated to developing a robust and modular framework for Multi-Agent Reinforcement Learning (MARL) algorithms. This project is a testament to my commitment to advancing research in MARL by focusing on modular design, code readability, and reproducibility of results.

## The Marl-Engineering Mission

Marl-Engineering is more than a codebase; it's an evolving platform for deep exploration and experimentation in the field of Deep MARL. It represents my journey in understanding and applying complex multi-agent systems and deep learning models. I approach this project not just as a developer but as a learner, deeply committed to comprehending every aspect of MARL.

This repository is designed to be modular, allowing researchers and enthusiasts to plug in different MARL algorithms and compare their performance in various settings. The focus on modularity also enables easier experimentation and adaptation of new methods and ideas in the field.

## Key Features

- **Modular Architecture**: Marl-Engineering is structured to support a range of MARL algorithms, with each component designed to be interchangeable and customizable. This modularity allows for extensive experimentation and adaptation.

- **Code Readability and Maintenance**: Emphasis is placed on clear, well-documented code to facilitate understanding and further development. This approach enhances the learning experience for those new to the field and maintains high standards for code quality.

- **Reproducibility of Results**: Ensuring the reproducibility of results is a core principle of Marl-Engineering. The repository is structured to enable researchers to replicate experiments and validate findings easily.

## Installation
It is necessary to install pysc2 before using this reporitory, please refer to:
> https://github.com/google-deepmind/pysc2
---
- Poetry installation
```
source activate_env.sh
```
- Docker installation (work in progress)
```
source install_docker.sh
```

## Experiments
- Run default configuration
```
python3 src/tune.py
```
or
```
python3 src/tune.py --config-name="trial.yaml"
```
- Run specific configuration
```
python3 src/tune.py --config-name="<defined-custom_config>.yaml"
```

## Applications and Use Cases

Marl-Engineering is ideal for tackling complex cooperative tasks that require coordination among multiple agents. Its applications span across various domains, such as strategic games, collaborative robotics, and multi-agent simulations. By providing a flexible and adaptable framework, Marl-Engineering aims to push the boundaries of what's possible in the realm of MARL.

## Join the Journey

As Marl-Engineering continues to grow, I plan to integrate cutting-edge technologies and methodologies to enhance its capabilities further. I invite collaborators, researchers, and enthusiasts to join me in this exciting journey of discovery and innovation in the world of Multi-Agent Reinforcement Learning.

## Reference
Some of the implementation ideas were taken from pymarl and pymarl2, you can refer to those sources in the links below:
> pymarl -> https://github.com/oxwhirl/pymarl <br />
> pymarl2 -> https://github.com/hijkzzz/pymarl2

## Citation

If you use this repository in your research, please cite it using the following BibTeX entry:

```bibtex
@misc{chojancki2023marl-engineering,
  title={marl-engineering},
  author={Chojancki, James},
  year={2023},
  publisher={GitHub},
  howpublished={\url{https://github.com/Sithael/marl-engineering}}
}
