FROM node:24-alpine
WORKDIR /app
ADD package*.json ./
RUN npm i
ADD . .
CMD node index.js