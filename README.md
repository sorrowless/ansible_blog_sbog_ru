sbog/blog_sbog_ru
=================

Role to install personal blog

#### Requirements

Ansible 2.4

#### Role Variables

```yaml
site_hostname: blog.sbog.ru
# Link to the main site from blog
mainsite_hostname: sbog.ru
origin_remote: https://github.com/sorrowless/blog_sbog_ru.git
# Path to certs dir
tls_path: /etc/ssl_certs
# Path to checkout source content to
git_dir: "/root/{{ site_hostname }}"
# Path to virtualenv
venv_dir: "{{ git_dir }}/.venv"
# Yandex metrika number
ya_metrika: 00000000
```

#### Dependencies

None

#### Example Playbook

```yaml
- name: Deploy personal blog to target host
  hosts: sbog_ru_webservers
  remote_user: root

  roles:
    - blog_sbog_ru
```

#### License

Apache 2.0

#### Author Information

Stanislaw Bogatkin (https://sbog.ru)
