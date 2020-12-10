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
        path: '/articles/:id',
        name: 'Article',
        component: Article,
        props: true
    },
    {
        path: '/articles/new',
        name: 'New Article',
        component: ArticleForm
    },
    {
        path: '/articles/:id/edit',
        name: 'Edit Article',
        component: ArticleForm,
        props: true
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
