# Certificate of Compliance Generator

A product developed by and for Hyrel Technologies. 
It's purpose is to be a locally hosted webserver to generate
certificate of compliance forms and to store all historically 
generated forms to log them. 

## Dependencies

Requires 
- Docker
- A basic Linux installation (WSL included)
- `uv` python pakage manager
- `bun.js` or `node.js` for related node cli commands

## Creating new templates

Use google docs to create the PDF and this 
[pdf form generator](https://tools.pdf24.org/en/create-fillable-pdf-form)
to generate the pdf fields used by this application.


To recreate this project with the same configuration:

```sh
# recreate this project
bun x sv@0.12.5 create --template demo --types ts --add prettier eslint playwright --install bun .
```

## Developing

Once you've created a project and installed dependencies with `bun install` (or `npm install` or `yarn`), start a development server:

```sh
bun run dev

# or start the server and open the app in a new browser tab
bun run dev -- --open
```

## Building

To create a production version of your app:

```sh
bun run build
```

You can preview the production build with `bun run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.

want coc? we got it