import dockerfile

run = """
RUN <<EOF
source $HOME/.bashrc && echo $HOME
EOF
"""

t = dockerfile.parse_string(run)

print(t)
