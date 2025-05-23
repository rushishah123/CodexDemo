FROM node:18
WORKDIR /app
COPY package.json tsconfig.json webpack.config.js ./
COPY public ./public
COPY src ./src
RUN npm install && npm run build
CMD ["npx", "webpack", "serve", "--mode", "development", "--host", "0.0.0.0"]
