FROM node:16

# Create app directory
WORKDIR /usr/src/app

COPY app/package-lock.json ./
COPY config/target/package.json ./

RUN npm install

# Bundle app source
COPY app .

EXPOSE 9997
CMD [ "node", "app.js" , "target"]