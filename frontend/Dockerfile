# Stage 1: Build the Angular application
FROM node:20 as build
WORKDIR /usr/local/app
COPY ./ /usr/local/app/
RUN npm install
RUN npm run build -- --configuration production

# Stage 2: Serve the application from Nginx
FROM nginx:alpine
COPY --from=build /usr/local/app/dist/frontend/browser /usr/share/nginx/html
EXPOSE 80