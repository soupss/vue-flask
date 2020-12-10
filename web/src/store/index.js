import { createStore } from 'vuex'

export default createStore({
    state: {
        articles: [],
        API_URL: 'http://localhost:5000/api/'
    },
    mutations: {
        setArticles(state, articles) {
            state.articles = articles
        }
    },
    actions: {
        // fetch all articles
        fetchArticles(context) {
            return fetch(context.state.API_URL + 'articles')
                .then(response => response.json())
                .then(data => data.articles)
        },
        fetchArticle(context, id) {
            return fetch(context.state.API_URL + 'articles/' + id + '/')
                .then(response => response.json())
                .then(data => data.article)
        },
        createArticle(context, article) {
            const requestOptions = {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(article)
            }
            fetch(context.state.API_URL + 'articles/', requestOptions)
        },
        deleteArticle(context, id) {
            const requestOptions = {
                method: 'DELETE'
            }
            return fetch(context.state.API_URL + 'articles/' + id + '/', requestOptions)
        }
    }
})
