# PM Simulator

## Introduction

Use AI models to adjust the products just like how PM does without coding.

## Installation

```
git clone https://github.com/tobegit3hub/pm_simulator.git

cd ./pm_simulator/

pip3 install -r ./requirements.txt
```

## Usage

Use the pre-built website for demo.

### Start Server

Setup OpenAI API Key to access GPT models.

```
export OPENAI_API_KEY=sk-xxx
```

Start the server.

```
cd ./pm_simulator/server/

./server.py
```

Open the website in `http://127.0.0.1:5000`.

### Use CLI

Use the command to change the website style.

```
cd ./pm_simulator/client/

./client.py "Change the background to blue"
./client.py "背景换成红色"
```

Refresh the website in `http://127.0.0.1:5000` to find out the changes.

You can use the [auto refresh extension](https://chrome.google.com/webstore/detail/easy-auto-refresh/aabcgdmkeabbnleenpncegpcngjpnjkc) to reload automatically.

### Use GUI

```
brew install dialog
```

```
./gui_toolbox.py
```
