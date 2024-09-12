import { createRouter, createWebHistory} from "vue-router";
import tecnicos from "@/components/tecnicos.vue"
import users from "@/components/users.vue"
import phones from "@/components/phones.vue";
import listSpareParts from "@/components/list-spare-parts.vue";
import spareParts from "@/components/spare-parts.vue";
import celForm from "@/components/cel-form.vue";
import check_list from "@/components/check_list.vue";

const routes=[
    {
        path:'/users',
        name: 'usuarios',
        component: users
    },
    {
        path:'/tec',
        name: 'tecnicos',
        component: tecnicos
    },
    {
        path:'/phones',
        name: 'phones',
        component: phones,
        children:[
            {
                path: "cel-form",
                component: celForm
            },
            {
                path: "check-list",
                component: check_list
            }
        ]
    },
    {
        path: '/listSpareParts',
        name: 'listSpareParts',
        component: listSpareParts
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router


