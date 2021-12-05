package com.innovatech.cart.models;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document
public class Carrito {
    @Id
    private String id;
    private String userId;
    private String productId;
    private Integer amount;
    private Float price;
}
