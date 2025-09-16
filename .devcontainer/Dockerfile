ARG BASE_IMAGE=nvidia/cuda:12.3.2-runtime-ubuntu22.04
FROM ${BASE_IMAGE}

# Create a non-root user
ARG USERNAME="dev"
ARG ROOT_DIR=/workspaces/projects/ConFusion

RUN useradd -m $USERNAME

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    cmake \
    git \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Miniconda (as root)
ARG CONDA_DIR=/opt/conda
ARG PATH=$CONDA_DIR/bin:$PATH

RUN apt-get update && apt-get install -y wget bzip2 && \
    wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh && \
    $CONDA_DIR/bin/conda clean -afy && \
    find $CONDA_DIR/ -follow -type f -name '*.a' -delete && \
    find $CONDA_DIR/ -follow -type f -name '*.js.map' -delete

# Fix update permissions for conda
RUN chown -R $USERNAME:$USERNAME /opt/conda

# Add conda to PATH for all users
ENV PATH=$CONDA_DIR/bin:$PATH

# Set the default shell
ENV SHELL=/bin/bash

# Set up the workspace directory
WORKDIR $ROOT_DIR

# Ensure correct permissions for workspace
RUN mkdir --parents build && \
    chown --recursive $USERNAME:$USERNAME $ROOT_DIR && \
    chmod --recursive 755 $ROOT_DIR

# Add the user to the input group
RUN groupadd -f input && \
    usermod -aG input $USERNAME

# Switch back to non-root user
USER $USERNAME

ENTRYPOINT ["$SHELL"]