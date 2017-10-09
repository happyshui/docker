#! /usr/bin/python2.7
# __*__ coding: utf-8 __*__


import json, requests, os


docker_registry_api = {"url": "http://172.16.234.101:5000/v2/"}


class Registry_API():
    def __init__(self, url):
        self.__url = url

    def Put(self, headers, data, urltype):
        url = self.__url + urltype
        headers = headers
        data = data
        requests.put(url, json=data, headers=headers)

    def Get(self, headers, data, urltype):
        url = self.__url + urltype
        headers = headers
        data = data
        res = requests.get(url, json=data, headers=headers)
        content =  json.loads(res.content)
        return content

    def Post(self, headers, data, urltype):
        url = self.__url + urltype
        headers = headers
        data = data
        requests.post(url, json=data, headers=headers)


def main():
    raction = Registry_API(url=docker_registry_api['url'])
    content = raction.Get(headers="",data="",urltype="_catalog")
    project_name = []
    l = 0
    for i in ["service-oauth2", "service-portal", "service-portal-test",
              "service-proxy", "service-turbine-test", "service-zipkin-test",
              "service-zuul", "sysmgt", "test-p2pcompliance", "test-p2pwebself", "third-huadao",
              "third-pengyuan", "third-qianhai", "third-rongshu", "third-zhongchengxin", "tomcat", "upload-file",
              "usermanage", "wd_web_api", "wd_web_front", "wd_web_server", "webapp", "webapp-l", "webapp-test", "webapp-tt",
              "webself", "workingpaper", "working-paper", "xinhunbao", "yuqing", "zhongchengxin", "zipkin"]:
        l = l+1
        t_list = i + "/tags/list"
        c = raction.Get(headers="", data="", urltype=t_list)
        for ii in c["tags"]:
            images =  "172.16.234.101:5000/" + c["name"] + ":" + ii
            p_name = images.split(":")[1].split("/")[1]
            if p_name[0:3] != "":
                newimages = "172.16.234.105/" + "library/" + c["name"] + ":" + ii
                docker_pull = "docker pull" + " " + images
                docker_tag = "docker tag" + " " + images + " " + newimages
                docker_push = "docker push" + " " + newimages
                os.system(docker_pull)
                os.system(docker_tag)
                os.system(docker_push)
            project_name.append(p_name)

if __name__ == '__main__':
    main()