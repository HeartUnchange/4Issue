import Vue from 'vue';
import {Loading} from 'element-ui';
import ElementUI from 'element-ui';
import VueRouter from 'vue-router';

import 'element-ui/lib/theme-chalk/index.css';

const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }

const routes = [
    { path: '/foo', component: Foo },
    { path: '/bar', component: Bar }
  ]


import App from './App.vue'

Vue.use(VueRouter);
Vue.use(ElementUI)


// 路由配置
const RouterConfig = {
  mode: 'history',
  routes: routes
};
const router = new VueRouter(RouterConfig);

router.beforeEach((to, from, next) => {
  let loadingInstance = Loading.service({ fullscreen: true });
  next();
});

router.afterEach((to, from) => {
  let loadingInstance = Loading.service({ fullscreen: true });
  loadingInstance.close();
});

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});
