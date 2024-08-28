import { reactive, ref } from 'vue';

const location_ditecter = ref(localStorage.getItem('location_ditecter'));
const openpop = ref(false);
export const store = reactive({
    location_ditecter:location_ditecter.value,
    openpop:openpop.value
});
