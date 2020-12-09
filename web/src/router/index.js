import { createRouter, createWebHashHistory } from 'vue-router'
import ArticlePreviewsView from '../views/ArticlePreviewsView.vue'
import ArticleView from '../views/ArticleView.vue'
import NewArticleView from '../views/NewArticleView.vue'

const routes = [
    {
        path: '/',
        redirect: '/articles',
    },
    {
        path: '/articles',
        name: 'Article Previews',
        component: ArticlePreviewsView
    },
    {
        path: '/articles/new',
        name: 'New Article',
        component: NewArticleView
    },
    {
        path: '/article/:id',
        component: ArticleView,
        props: true
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
