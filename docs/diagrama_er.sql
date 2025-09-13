Table orders {
order_id varchar [pk]
customer_id varchar
}


Table customers {
customer_id varchar [pk]
customer_city varchar
customer_state varchar
}


Ref: orders.customer_id > customers.customer_id