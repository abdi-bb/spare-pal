FROM nginx:stable-alpine

RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.bak
COPY nginx.conf /etc/nginx/conf.d/

EXPOSE 80