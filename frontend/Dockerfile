FROM ghcr.io/cirruslabs/flutter:3.24.0 AS build
WORKDIR /app
COPY . .
RUN flutter pub get && flutter build web

FROM nginx:stable-alpine
COPY --from=build /app/build/web /usr/share/nginx/html
EXPOSE 80
