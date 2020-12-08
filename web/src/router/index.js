import { createRouter, createWebHashHistory } from 'vue-router'
import Articles from '../views/Articles.vue'
import NewArticle from '../views/NewArticle.vue'

const routes = [
    {
        path: '/articles',
        name: 'Articles',
        component: Articles
    },
    {
        path: '/articles/new',
        name: 'New Article',
        component: NewArticle
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
