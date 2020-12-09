import { createRouter, createWebHashHistory } from 'vue-router'
import ArticlesView from '../views/ArticlesView.vue'
import NewArticleView from '../views/NewArticleView.vue'

const routes = [
    {
        path: '/articles',
        name: 'Articles',
        component: ArticlesView
    },
    {
        path: '/articles/new',
        name: 'New Article',
        component: NewArticleView
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
