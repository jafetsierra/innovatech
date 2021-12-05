package com.innovatech.cart.models;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document
public class Producto {
    @Id
    private String id;
    private String name;
    private String description;
    private Float price;
    private String category;
    private Integer stock;
}
