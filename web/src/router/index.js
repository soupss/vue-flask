import { createRouter, createWebHashHistory } from 'vue-router'
import ArticlePreviews from '../views/ArticlePreviews.vue'
import Article from '../views/Article.vue'
import ArticleForm from '../views/ArticleForm.vue'

const routes = [
    {
        path: '/',
        redirect: '/articles',
    },
    {
        path: '/articles',
        name: 'Article Previews',
        component: ArticlePreviews
    },
    {
        path: '/article/:id',
        component: Article,
        props: true
    },
    {
        path: '/articles/new',
        name: 'New Article',
        component: ArticleForm
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
