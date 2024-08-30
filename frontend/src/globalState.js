import { reactive, ref } from 'vue';

const location_ditecter = ref(localStorage.getItem('location_ditecter'));
const openpop = ref(false);
const cart_count = ref(0);
const address = ref(localStorage.getItem('address'));;
export const store = reactive({
    location_ditecter:location_ditecter.value,
    openpop:openpop.value,
    address:address.value,
    cart_count:cart_count.value,
});
