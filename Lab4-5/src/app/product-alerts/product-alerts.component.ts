import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Product } from '../products'; // <- maybe delete

@Component({
  selector: 'app-product-alerts',
  templateUrl: './product-alerts.component.html',
  styleUrls: ['./product-alerts.component.css'],
})
export class ProductAlertsComponent {
  @Input() product: Product | undefined;
  @Output() notify = new EventEmitter();

  // @Input() product!: Product;
  // constructor() {}

  // ngOnInit(): void {}

  // @Input() product: Product | undefined;
  // @Output() notify = new EventEmitter();
}
